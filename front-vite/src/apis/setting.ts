import http from '@/utils/http';

export interface University {
  name: string;
  level: string;
}

export interface Major {
  name: string;
  category: string;
}

export interface Personnel {
  name: string;
  recruitment_type: string;
  department: string;
  research_direction: string;
  order: number;
}

export interface Award {
  name: string;
  level: string;
  category: string;
}

// 获取所有院校配置
export const getUniversities = () => {
  return http.get<University[]>('/api/settings/universities/');
};

// 更新院校配置
export const updateUniversities = (universities: University[]) => {
  return http.post('/api/settings/universities/', universities);
};

// 获取所有专业配置
export const getMajors = () => {
  return http.get<Major[]>('/api/settings/majors/');
};

// 更新专业配置
export const updateMajors = (majors: Major[]) => {
  return http.post('/api/settings/majors/', majors);
};

// 获取所有人员配置
export const getPersonnel = () => {
  return http.get<Personnel[]>('/api/settings/personnel/');
};

// 更新人员配置
export const updatePersonnel = (personnel: Personnel[]) => {
  return http.post('/api/settings/personnel/', personnel);
};

// 获取所有奖项配置
export const getAwards = () => {
  return http.get<Award[]>('/api/settings/awards/');
};

// 更新奖项配置
export const updateAwards = (awards: Award[]) => {
  return http.post('/api/settings/awards/', awards);
};

// 获取年份 - 返回数字类型
export const getYear = () => {
  return http.get<number>('/api/settings/year/');
};

// 更新年份 - 接收数字参数
export const updateYear = (year: number) => {
  return http.post('/api/settings/year/', { year });
};