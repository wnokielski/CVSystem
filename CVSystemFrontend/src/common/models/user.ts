export class User {
  first_name: string;
  last_name: string;
  email_address: string;
  password: string;
  birth_date: Date;
  account_type: string;

  constructor(fn: string, ln: string, e: string, p: string, bd: Date, at: string) {
    this.first_name = fn;
    this.last_name = ln;
    this.email_address = e;
    this.password = p;
    this.birth_date = bd;
    this.account_type = at;
  }
}
