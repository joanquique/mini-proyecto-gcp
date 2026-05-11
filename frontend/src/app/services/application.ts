import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import {
  Application,
  CreateApplication,
  UpdateApplication
} from '../models/application.model';

@Injectable({
  providedIn: 'root'
})
export class ApplicationService {
  private readonly apiUrl = 'https://gcp-fullstack-backend-588231403889.us-central1.run.app/applications';

  constructor(private http: HttpClient) {}

  getApplications(): Observable<Application[]> {
    return this.http.get<Application[]>(`${this.apiUrl}/`);
  }

  getApplicationById(id: number): Observable<Application> {
    return this.http.get<Application>(`${this.apiUrl}/${id}`);
  }

  createApplication(application: CreateApplication): Observable<Application> {
    return this.http.post<Application>(`${this.apiUrl}/`, application);
  }

  updateApplication(
    id: string,
    application: UpdateApplication
  ): Observable<Application> {
    return this.http.put<Application>(`${this.apiUrl}/${id}`, application);
  }

  deleteApplication(id: string): Observable<{ message: string }> {
    return this.http.delete<{ message: string }>(`${this.apiUrl}/${id}`);
  }
}
