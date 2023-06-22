import {Component} from '@angular/core';
import {API_URL} from "../../common/consts";
import {UserDetails} from "../../common/models/user";
import {HttpClient} from "@angular/common/http";
import {Router} from "@angular/router";
import {StateService} from "../state.service";
import {Offer} from "../../common/models/offer";
import {NewApplication} from "../../common/models/application";

@Component({
  selector: 'app-offers',
  templateUrl: './offers.component.html',
  styleUrls: ['./offers.component.css']
})
export class OffersComponent {

  offers: Offer[] = [];

  constructor(private http: HttpClient,
              private router: Router,
              private stateService: StateService) {

    // recieve user details

    if (this.stateService.userID != 0) {
      this.http.get(`${API_URL}/users/${this.stateService.userID}`).subscribe(
        response => {
          console.log('Response:', response)
          const userDetails = response as UserDetails
          this.stateService.isUserLoggedIn = true
          this.stateService.userName = userDetails.first_name
          this.stateService.accountType = userDetails.account_type
        },
        error => {
          console.error('Error:', error);
          alert(error.error.detail)
        }
      );
    }

    this.http.get(`${API_URL}/offers/all`).subscribe(
      response => {
        console.log('Response:', response)
        this.offers = (response) as Offer[]
      },
      error => {
        console.error('Error:', error);
        alert(error.error.detail)
      }
    );
  }

  isUserTypeApplicant() {
    console.log(`User type: ${this.stateService.accountType}`)
    console.log(this.stateService.accountType == "applicant")
    return this.stateService.accountType == "applicant"
  }

  applyForOffer(offer: any) {
    this.http.post(`${API_URL}/applications`, new NewApplication(offer.id, this.stateService.userID)).subscribe(
      response => {
        console.log('Response:', response);
      },
      error => {
        console.error('Error:', error);
        alert(error.error.detail)
      }
    );
    console.log('Applied for offer:', offer.id);
  }

}
