import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class StateService {

  private _isUserLoggedIn = false;
  private _userName: string = ""
  private _userID: number = 0
  private _accountType: string = ""

  get isUserLoggedIn(): boolean {
    return this._isUserLoggedIn;
  }

  set isUserLoggedIn(value: boolean) {
    this._isUserLoggedIn = value;
  }

  get userName(): string {
    return this._userName;
  }

  set userName(value: string) {
    this._userName = value;
  }

  get userID(): number {
    return this._userID;
  }

  set userID(value: number) {
    this._userID = value;
  }

  get accountType(): string {
    return this._accountType;
  }

  set accountType(value: string) {
    this._accountType = value;
  }

  constructor() { }
}
