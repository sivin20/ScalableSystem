import { Routes } from '@angular/router';
import { WelcomePage } from '../routes/welcome-page/welcome-page.component';
import {TaxiPricePageComponent} from "../routes/taxi-price-page/taxi-price-page.component";

export const routes: Routes = [
  { path: '', component: WelcomePage },
  { path: 'taxiprice', component: TaxiPricePageComponent}
];
