import http from '../utils/http';

export interface PercentData {
  pOfA: number;
  pOfB: number;
  pOfC: number;
  pOfATop: number;
  pOfBTop: number;
  pOfCTop: number;
  pOfATalent: number;
  pOfBTalent: number;
  pOfCTalent: number;
}

// 获取百分比数据（只有一行记录）
export const getPercent = () => {
  return http.get<PercentData>('/api/percent/');
};

// 更新百分比数据
export const updatePercent = (data: PercentData) => {
  return http.put<PercentData>('/api/percent/1/', data);
};