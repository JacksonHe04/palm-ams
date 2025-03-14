import { Entity, PrimaryGeneratedColumn, Column } from 'typeorm';

@Entity({ name: 'test_student' })
export class Student {
  @PrimaryGeneratedColumn()
  id: number;

  @Column()
  name: string;

  @Column()
  age: number;

  @Column()
  grade: string;
}
