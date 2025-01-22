// src/app/app.controller.ts
import { Controller, Get, HttpCode, HttpStatus } from '@nestjs/common';

@Controller('api')
export class AppController {
  @Get()
  @HttpCode(HttpStatus.OK)
  getApiRoot() {
    return {
      status: HttpStatus.OK,
      message: 'API Root',
    };
  }
}