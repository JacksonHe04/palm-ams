// src/apis/applyStore.ts
import http from '@/utils/http.ts';

export function submitApplication(data) {
  return http.post('/api/apply/', data);
}
