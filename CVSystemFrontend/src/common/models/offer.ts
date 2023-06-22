export class Offer {
  id: number;
  companyName: string;
  position: string;
  constructor(id: number, company_name: string, position: string) {
    this.id = id;
    this.companyName = company_name;
    this.position = position;
  }
}
