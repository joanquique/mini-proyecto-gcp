import { Component, OnInit } from '@angular/core';
import { ApplicationService } from './services/application';
import { Application } from './models/application.model';
import { ReactiveFormsModule, FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-root',
  imports: [ReactiveFormsModule],
  templateUrl: './app.html',
  styleUrl: './app.scss'
})
export class App implements OnInit {
  applications: Application[] = [];
  applicationForm: FormGroup;
  loading = true;
  error = '';

  constructor(private applicationService: ApplicationService,
    private fb: FormBuilder
  ) {
    this.applicationForm = this.fb.group({
      company: ['', Validators.required],
      position: ['', Validators.required],
      status: ['Pendiente', Validators.required],
      notes: ['']
    });
  }

  ngOnInit(): void {
    this.loadApplications();
  }

  loadApplications(): void {
    this.applicationService.getApplications().subscribe({
      next: (data) => {
        this.applications = data;
        this.loading = false;
      },
      error: () => {
        this.error = 'No se pudieron cargar las postulaciones';
        this.loading = false;
      }
    });
  }
  createApplication(): void {
    if (this.applicationForm.invalid) {
      this.applicationForm.markAllAsTouched();
      return;
    }

    this.applicationService.createApplication(this.applicationForm.value).subscribe({
      next: (newApplication) => {
        this.applications = [...this.applications, newApplication];
        this.applicationForm.reset({
          company: '',
          position: '',
          status: 'Pendiente',
          notes: ''
        });
      },
      error: () => {
        this.error = 'No se pudo crear la postulación';
      }
    });
  }
  deleteApplication(id: number): void {
    const confirmDelete = confirm('¿Seguro que quieres eliminar esta postulación?');

    if (!confirmDelete) {
      return;
    }

    this.applicationService.deleteApplication(id).subscribe({
      next: () => {
        this.applications = this.applications.filter(
          application => application.id !== id
        );
      },
      error: () => {
        this.error = 'No se pudo eliminar la postulación';
      }
    });
  }
}