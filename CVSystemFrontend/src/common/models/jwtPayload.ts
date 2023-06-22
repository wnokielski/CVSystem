export class JwtPayload {
  token: string;
  user_id: number;

  constructor(t: string, uid: number) {
    this.token = t;
    this.user_id = uid;
  }
}
