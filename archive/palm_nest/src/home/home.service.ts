import { Injectable } from '@nestjs/common';

@Injectable()
export class HomeService {
  async getWelcomeData() {
    // 这里可以是从数据库或其他服务获取的数据
    return {
      message: 'Welcome to the Palm Admissions System front-desk!',
      timestamp: new Date(),
    };
  }
}
