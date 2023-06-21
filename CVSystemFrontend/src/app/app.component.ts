import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  isUserLoggedIn = false;

  login() {
    // Logika logowania
    // Po poprawnym zalogowaniu ustaw wartość isUserLoggedIn na true
    this.isUserLoggedIn = true;
  }

  logout() {
    // Logika wylogowania
    // Po wylogowaniu ustaw wartość isUserLoggedIn na false
    this.isUserLoggedIn = false;
  }
}
