import { Component } from '@angular/core';
import { TaxiPriceService } from '../../services/taxi-price.service';
import {RouterLink} from "@angular/router";

@Component({
    selector: 'app-front-page',
    standalone: true,
  imports: [
    RouterLink
  ],
    templateUrl: './welcome-page.component.html',
    styleUrl: './welcome-page.component.scss'
})
export class WelcomePage {

    constructor () {}

}
