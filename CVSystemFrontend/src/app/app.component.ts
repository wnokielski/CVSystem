import { Component } from '@angular/core';
import {StateService} from "./state.service";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {

  constructor(private stateService: StateService) {
  }

  userLoggedIn() {
    return this.stateService.isUserLoggedIn
  }

  loggedUserName() {
    return this.stateService.userName
  }

}
