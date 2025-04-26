import http from '@/utils/http';

export interface AdmissionDate {
  type: string;
  start_time: string;  // 改为 start_time
  end_time: string;    // 改为 end_time
}

/**
 * 获取招生时间配置列表
 */
export const getAdmissionDates = () => {
  return http.get<AdmissionDate[]>('/api/date/admission-dates/');
};

/**
 * 更新招生时间配置
 * @param dates - 招生时间配置列表
 */
export const updateAdmissionDates = (dates: AdmissionDate[]) => {
  return http.post('/api/date/admission-dates/', dates);
};

/**
 * 根据年份获取招生时间配置
 * @param year - 年份
 */
export const getAdmissionDatesByYear = (year: number) => {
  return http.get<AdmissionDate[]>(`/api/date/admission-dates/${year}/`);
};

/**
 * 更新指定年份的招生时间配置
 * @param year - 年份
 * @param dates - 招生时间配置列表
 */
export const updateAdmissionDatesByYear = (year: number, dates: AdmissionDate[]) => {
  return http.post(`/api/date/admission-dates/${year}/update_year/`, dates);
};