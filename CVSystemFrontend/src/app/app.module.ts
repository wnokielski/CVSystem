import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { CommonModule } from '@angular/common';

import { AppComponent } from './app.component';
import { RegistrationComponent } from './registration/registration.component';
import {FormsModule} from "@angular/forms";
import { AppRoutingModule } from './app-routing.module';
import { LoginComponent } from './login/login.component';
import { OffersComponent } from './offers/offers.component';
import { ApplicationsComponent } from './applications/applications.component';
import { HomeComponent } from './home/home.component';
import {HttpClient, HttpClientModule} from "@angular/common/http";
import {StateService} from "./state.service";

@NgModule({
  declarations: [
    AppComponent,
    RegistrationComponent,
    LoginComponent,
    OffersComponent,
    ApplicationsComponent,
    HomeComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    AppRoutingModule,
    HttpClientModule,
    CommonModule
  ],
  providers: [HttpClient, StateService],
  bootstrap: [AppComponent]
})
export class AppModule { }
