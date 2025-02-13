// src/management/entities/apply.entity.ts
import { Entity, Column, PrimaryColumn } from 'typeorm';

@Entity({ name: 'students' })
export class Apply {
  @PrimaryColumn({ length: 50 })
  id: string;

  @Column({ length: 50 })
  name: string;

  @Column('int')
  graduationYear: number;

  @Column({ length: 10 })
  gender: string;

  @Column({ length: 20 })
  birthDate: string;

  @Column()
  photo: string;

  @Column({ length: 50 })
  university: string;

  @Column({ length: 50 })
  major: string;

  @Column('int')
  majorCount: number;

  @Column('int')
  rank: number;

  @Column({ length: 10 })
  percentage: string;

  @Column({ length: 50 })
  masterUniversity: string;

  @Column({ length: 50 })
  masterMajor: string;

  @Column({ length: 50 })
  tutor: string;

  @Column({ length: 50 })
  phone: string;

  @Column({ length: 100 })
  email: string;

  @Column({ length: 50 })
  applicationType: string;

  @Column({ length: 50 })
  firstChoice: string;

  @Column({ length: 50 })
  secondChoice: string;

  @Column({ length: 50 })
  thirdChoice: string;

  @Column('boolean') // 修改为 'boolean'
  isAdjustable: boolean;

  @Column({ length: 255 })
  proofs: string;

  @Column({ length: 50 })
  status: string;

  // Paper fields
  @Column({ length: 7, nullable: true })
  paper1_publicationTime: string;

  @Column({ length: 100, nullable: true })
  paper1_journalConference: string;

  @Column({ length: 100, nullable: true })
  paper1_paperName: string;

  @Column({ length: 10, nullable: true })
  paper1_ccfLevel: string;

  @Column({ length: 50, nullable: true })
  paper1_awardCategory: string;

  @Column({ length: 7, nullable: true })
  paper2_publicationTime: string;

  @Column({ length: 100, nullable: true })
  paper2_journalConference: string;

  @Column({ length: 100, nullable: true })
  paper2_paperName: string;

  @Column({ length: 10, nullable: true })
  paper2_ccfLevel: string;

  @Column({ length: 50, nullable: true })
  paper2_awardCategory: string;

  @Column({ length: 7, nullable: true })
  paper3_publicationTime: string;

  @Column({ length: 100, nullable: true })
  paper3_journalConference: string;

  @Column({ length: 100, nullable: true })
  paper3_paperName: string;

  @Column({ length: 10, nullable: true })
  paper3_ccfLevel: string;

  @Column({ length: 50, nullable: true })
  paper3_awardCategory: string;

  // Award fields
  @Column('boolean', { nullable: true }) // 修改为 'boolean'
  award1_isLeader: boolean;

  @Column({ length: 7, nullable: true })
  award1_awardTime: string;

  @Column({ length: 100, nullable: true })
  award1_awardName: string;

  @Column({ length: 50, nullable: true })
  award1_levelRanking: string;

  @Column({ length: 50, nullable: true })
  award1_awardRanking: string;

  @Column('boolean', { nullable: true }) // 修改为 'boolean'
  award2_isLeader: boolean;

  @Column({ length: 7, nullable: true })
  award2_awardTime: string;

  @Column({ length: 100, nullable: true })
  award2_awardName: string;

  @Column({ length: 50, nullable: true })
  award2_levelRanking: string;

  @Column({ length: 50, nullable: true })
  award2_awardRanking: string;

  @Column('boolean', { nullable: true }) // 修改为 'boolean'
  award3_isLeader: boolean;

  @Column({ length: 7, nullable: true })
  award3_awardTime: string;

  @Column({ length: 100, nullable: true })
  award3_awardName: string;

  @Column({ length: 50, nullable: true })
  award3_levelRanking: string;

  @Column({ length: 50, nullable: true })
  award3_awardRanking: string;

  @Column({ length: 50, nullable: true })
  universityLevel: string;

  @Column({ length: 50, nullable: true })
  masterUniversityLevel: string;
}
