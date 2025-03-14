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
}

export interface AdmissionPeriod {
  startDate: string;
  endDate: string;
}

export interface Award {
  name: string;
  level: string;
  category: string;
}

export interface Year {
  year: string;
  status: string;
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

// 获取招生时间配置
export const getAdmissionPeriod = () => {
  return http.get<AdmissionPeriod>('/api/settings/admission-period/');
};

// 更新招生时间配置
export const updateAdmissionPeriod = (period: AdmissionPeriod) => {
  const transformedData = {
    start_date: period.startDate,
    end_date: period.endDate
  };
  return http.post('/api/settings/admission-period/', transformedData);
};

// 获取所有奖项配置
export const getAwards = () => {
  return http.get<Award[]>('/api/settings/awards/');
};

// 更新奖项配置
export const updateAwards = (awards: Award[]) => {
  return http.post('/api/settings/awards/', awards);
};

// 获取所有年份配置
export const getYears = () => {
  return http.get<Year[]>('/api/settings/years/');
};

// 更新年份配置
export const updateYears = (years: Year[]) => {
  return http.post('/api/settings/years/', years);
};