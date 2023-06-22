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

export class UserDetails {
  first_name: string;
  last_name: string;
  email_address: string;
  account_type: string;

  constructor(first_name: string, last_name: string, email_address: string, account_type: string) {
    this.first_name = first_name;
    this.last_name = last_name;
    this.email_address = email_address;
    this.account_type = account_type;
  }
}
