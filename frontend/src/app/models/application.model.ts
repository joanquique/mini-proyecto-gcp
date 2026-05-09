export interface Application {
  id: number;
  company: string;
  position: string;
  status: string;
  notes?: string | null;
  created_at: string;
}

export interface CreateApplication {
  company: string;
  position: string;
  status: string;
  notes?: string | null;
}

export interface UpdateApplication {
  company?: string;
  position?: string;
  status?: string;
  notes?: string | null;
}