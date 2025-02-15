// src/apis/applyStore.ts
import http from '@/utils/http';

export function submitApplication(data) {
  return http.post('/api/apply/', data);
}
