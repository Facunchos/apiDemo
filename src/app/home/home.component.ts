import { Component, OnInit } from '@angular/core';
import { ApiService } from '../service/api.service';
import { NgFor } from '@angular/common';
  @Component({
  selector: 'app-home',
  standalone: true,
  imports: [NgFor],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent implements OnInit {
  data: any[] = [];

  constructor(private apiService: ApiService){}

  ngOnInit(): void {
    this.llenarData()
  }
  llenarData(){
    this.apiService.getData().subscribe(data => {
      this.data = data.results;
      console.log('data', this.data);
    })
  }
}
