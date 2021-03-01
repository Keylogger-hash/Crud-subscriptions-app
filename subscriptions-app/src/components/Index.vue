<template>
  <div class="pt-5">
    <div v-if="subscriptions.length!=0 && subscriptions">
      <div class="card mb-3" v-for="(sub,index) of subscriptions" v-bind:key="sub.id">
          <div class="row no-gutters">
            <div class="col-md-4">
              <img  :height="200" class="card-img" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTPhET_10JHX83dkNn1tMFWCZ8Ei6ZbEHkdPQ&usqp=CAU">
            </div>
            <div class="col-md-8">
              <div class="card-body">
                <h5 class="card-title">{{sub.name}}</h5>
                <p class="card-text">{{sub.description}}</p>
                <router-link :to="{name:'edit', params:{id:sub.id}}" class="btn btn-sm btn-primary">Edit</router-link>
                <button class="btn btn-sm btn-danger" @click="deleteSubscription(sub)">Delete</button><br/>
                <div class="accordion" role="tablist">
                  <b-card nobody class="mb-1">
                    <b-card-header header-tag="header" class="p-1" role="tab">
                      <b-button block v-b-toggle="'accordion'+index" variant="info">Show more</b-button>
                    </b-card-header>
                    <b-collapse :id="'accordion'+index" :accordion="'my-accordion'+index" role="tabpanel">
                      <b-card-body>
                        <b-card-title>Name:{{sub.name}}</b-card-title>
                        <b-card-text>Price:{{sub.price}}</b-card-text>
                        <b-card-text>Currency:{{sub.currency}}</b-card-text>
                        <b-card-text>Description:{{sub.description}}</b-card-text>
                      </b-card-body>
                    </b-collapse>
                  </b-card>
                </div>
              </div>

            </div>
          </div>
        </div>
    </div>
    <p v-else-if="subscriptions.length==0">No subscriptions</p>
  </div>
</template>


<script>
import axios from "axios"
export default {
  name:"Index",
  data() {
    return {
      subscriptions: [],
      states:[false,false,false]
    }
  },
  created() {
    this.all()
  },
  methods: {
    deleteSubscription: function(subrc) {
      if(confirm('Delete'+subrc.name)) {
        axios.delete(`http://127.0.0.1:8000/api/subscriptions/${subrc.id}/`).then(response=>{
          this.all()
          // console.log(subrc)
          console.log(response)
        })
      }

    },
    doSomething: function(event,i) {
      console.log("clicked item"+i)
    },
    all:function() {
      axios.get("http://127.0.0.1:8000/api/subscriptions/").then(response=>{
        this.subscriptions=response.data
      })
    }
  }
}
</script>
<style>
@import url('https://fonts.googleapis.com/css?family=Open+Sans');

.button, .card-text, .card-header{
  font-family: 'Open Sans', sans-serif;
}
/* .container {
  margin:10px;
  padding:30px;
}

.card{
  width: 20rem;
  border-top-right-radius: 10px 10px;
  border-top-left-radius: 50px 50px;
  border-bottom-left-radius: 5px 5px;
  border-bottom-right-radius: 50px 50px;
  box-shadow: 2px 2px 15px 2px #ccc;
}
.img {
  border-top-right-radius: 5px 5px;
 border-top-left-radius: 50px 50px;
} */

</style>
