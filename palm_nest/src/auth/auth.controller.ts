// src/auth/auth.controller.ts
import { Controller, Post, Body, HttpException, HttpStatus } from '@nestjs/common';
import { AuthService } from './auth.service';
import { User } from './user.entity';

@Controller('api')
export class AuthController {
  constructor(private authService: AuthService) {}

  @Post('login')
  async login(@Body() user: User) {
    const result = await this.authService.validateUser(user.username, user.password);
    if (!result) {
      throw new HttpException('Invalid credentials', HttpStatus.UNAUTHORIZED);
    }
    return {
      message: 'login successful',
      user: result,
    };
  }

  @Post('register')
  async register(@Body() user: User) {
    try {
      const result = await this.authService.register(user);
      return {
        message: 'Registration successful',
        user: result,
      };
    } catch (error) {
      throw new HttpException('Registration failed', HttpStatus.INTERNAL_SERVER_ERROR);
    }
  }
}
