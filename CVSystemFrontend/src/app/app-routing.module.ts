import {NgModule} from '@angular/core';
import {RegistrationComponent} from "./registration/registration.component";
import {RouterModule, Routes} from "@angular/router";
import {LoginComponent} from "./login/login.component";
import {OffersComponent} from "./offers/offers.component";
import {ApplicationsComponent} from "./applications/applications.component";
import {HomeComponent} from "./home/home.component";


const routes: Routes = [
  {path: 'registration', component: RegistrationComponent},
  {path: 'login', component: LoginComponent},
  {path: 'offers', component: OffersComponent},
  {path: 'applications', component: ApplicationsComponent},
  {path: 'home', component: HomeComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {
}