import { Injectable } from '@angular/core';
import { HttpClient } from "@angular/common/http";


@Injectable({
	providedIn: 'root'
})
export class TaxiPriceService {

	constructor(
		private http: HttpClient,

	) { }


	async getPrice(): Promise<number> {
		return new Promise(async (resolve: any, reject: any) => {
			return this.http.get(`http://127.0.0.1:8000`).toPromise().then((res) => {
				return resolve(res)
			}).catch((err) => {
				return reject(err);
			})
		})
	}
}
