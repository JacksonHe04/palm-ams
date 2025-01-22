// src/home/home.controller.ts
import { Controller, Get, HttpCode, HttpStatus } from '@nestjs/common';
import { HomeService } from './home.service';

@Controller('api')
export class HomeController {
  constructor(private readonly testService: HomeService) {}

  @Get('home/welcome')
  @HttpCode(HttpStatus.OK)
  async getWelcomeData() {
    try {
      const data = await this.testService.getWelcomeData();
      return {
        status: HttpStatus.OK,
        data,
      };
    } catch (error) {
      return {
        status: HttpStatus.INTERNAL_SERVER_ERROR,
        message: 'Internal Server Error',
      };
    }
  }
}
