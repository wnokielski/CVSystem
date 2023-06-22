export class Application {
  id: number;
  applicant_id: number;
  offer_id: number;
  status: string;
  recruiter_id: number;
  resume_id: number;
  constructor(id: number, applicant_id: number, offer_id: number, status: string, recruiter_id: number, resume_id: number) {
    this.id = id;
    this.applicant_id = applicant_id;
    this.offer_id = offer_id;
    this.status = status;
    this.recruiter_id = recruiter_id;
    this.resume_id = resume_id;
  }
}

export class NewApplication {
  constructor(offer_id: number, applicant_id: number) {
    this.offer_id = offer_id;
    this.applicant_id = applicant_id;
  }
  offer_id: number;
  applicant_id: number;
}
