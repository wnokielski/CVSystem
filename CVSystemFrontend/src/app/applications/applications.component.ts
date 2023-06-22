import { Component } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Router} from "@angular/router";
import {StateService} from "../state.service";
import {Application} from "../../common/models/application";
import {API_URL} from "../../common/consts";

@Component({
  selector: 'app-applications',
  templateUrl: './applications.component.html',
  styleUrls: ['./applications.component.css']
})
export class ApplicationsComponent {

  applications: Application[] = [];
  constructor(private http: HttpClient,
              private router: Router,
              private stateService: StateService) {

    // get applications

    this.http.get(`${API_URL}/applications/byUser/${this.stateService.accountType}/${this.stateService.userID}`).subscribe(
      response => {
        console.log('Response:', response)
        this.applications = (response) as Application[]
      },
      error => {
        console.error('Error:', error);
        alert(error.error.detail)
      }
    );
  }

  isUserTypeApplicant() {
    return this.stateService.accountType == "applicant"
  }

  acceptApplication(app : Application) {
    this.http.patch(`${API_URL}/applications/accept/${app.id}`, null).subscribe(
      response => {
        console.log('Response:', response);
      },
      error => {
        console.error('Error:', error);
        alert(error.error.detail)
      }
    );
    console.log("Accepted application: "+app.id)
  }

  rejectApplication(app : Application) {
    this.http.patch(`${API_URL}/applications/reject/${app.id}`, null).subscribe(
      response => {
        console.log('Response:', response);
      },
      error => {
        console.error('Error:', error);
        alert(error.error.detail)
      }
    );
    console.log("Rejected application: "+app.id)
  }

}
