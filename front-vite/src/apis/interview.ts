import http from '../utils/http';

export interface InterviewScore {
  student: string;
  scoreTeacher1: number;
  scoreTeacher2: number;
  scoreTeacher3: number;
  normalizedScore?: number;
  resumeScore?: number;
}

// 上传面试评分Excel文件
export const uploadInterviewScores = async (file: File) => {
  const formData = new FormData();
  formData.append('file', file);
  return http.post('/api/interview/upload', formData, {
    headers: {
      'Content-Type': 'multipart/form-data',
    },
  });
};

// 获取归一化后的面试评分
export const getNormalizedScores = async () => {
  return http.get('/api/interview/normalized');
};