import {Component, OnDestroy, OnInit} from '@angular/core';
import {TaxiPriceService} from "../../services/taxi-price.service";
import {RouterLink} from "@angular/router";
import {FormBuilder, FormsModule, ReactiveFormsModule, Validators} from "@angular/forms";
import moment from 'moment';
import {DatePipe} from "@angular/common";

interface day {
  id: number,
  day: string,
}

interface details {
  duration: number,
  distance: number,
  //weather: string
}
@Component({
  selector: 'app-taxi-price-page',
  standalone: true,
  imports: [
    RouterLink,
    FormsModule,
    ReactiveFormsModule,
    DatePipe
  ],
  templateUrl: './taxi-price-page.component.html',
  styleUrl: './taxi-price-page.component.scss'
})
export class TaxiPricePageComponent implements OnInit, OnDestroy {

  price: string = '-'

  priceForm: any

  days: day[] = [
    {id: 1, day: 'Monday'},
    {id: 2, day: 'Tuesday'},
    {id: 3, day: 'Wednesday'},
    {id: 4, day: 'Thursday'},
    {id: 5, day: 'Friday'},
    {id: 6, day: 'Saturday'},
    {id: 7, day: 'Sunday'}
  ]

  weathers: string[] = [
    'clear',
    'sunny',
    'rain'
  ]
  constructor (
    public taxiPriceService: TaxiPriceService,
    private formBuilder: FormBuilder
  ) {}

  ngOnInit(): void {
    this.priceForm = this.formBuilder.group({
      distance: [null, Validators.required],
      duration: [null, [Validators.required]],
      //weather: [null, Validators.required],
    });
    this.intervalId = setInterval(() => {
      this.time = moment().subtract(5, 'months').subtract(7, 'years').toDate()
    }, 1000);
  }

  time = moment().subtract(1, 'months').subtract(7, 'years').toDate()
  intervalId: any;


  ngOnDestroy() {
    clearInterval(this.intervalId);
  }

  submitForm(): void {
    if (this.priceForm.valid) {
      const details: details = {
        distance: this.priceForm.value.distance,
        duration: this.priceForm.value.duration,
        //weather: this.priceForm.value.weather
      }
      this.getPrice(details)
    } else {
      console.log("not valid")
    }
  }
  async getPrice(details: details) {
    const params: string = `start=${moment().unix()-moment().startOf('day').unix()}&duration=${details.duration}&distance=${details.distance}`
    this.price = (await this.taxiPriceService.getPrice(params)).price.toFixed(2)
  }
}
