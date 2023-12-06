import { Component } from '@angular/core';
import { FontPageService } from '../../services/font-page.service';

@Component({
    selector: 'app-front-page',
    standalone: true,
    imports: [],
    templateUrl: './front-page.component.html',
    styleUrl: './front-page.component.css'
})
export class FrontPageComponent {

    value: string = 'Not callled'


    constructor (
        public frontPageService: FontPageService, // used in html
    ) {
    }

    async test() {
        this.value = await this.frontPageService.test() as string
    }
}
