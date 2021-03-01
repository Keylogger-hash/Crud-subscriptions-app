<template>
  <div class="pt-5">
    <form @submit.prevent="create" method="POST">
      <div class="form-group">
        <label for="name">Name</label>
        <input
        type="text"
        class="form-control"
        id="name"
        v-model="subscription.name"
        name="name"
        placeholder="Enter name:"
        v-validate="'required'"
        >
        <div class="invalid-feedback">
          Please a proide a name
        </div>
      </div>
      <div class="form-group">
        <label for="currency">currency</label>
        <select
        name="currency"
        type="text"
        class="form-control"
        id="currency"
        v-model="subscription.currency"
        v-validate="'required'"
        >
        <option value="EUR">EUR</option>
        <option value="RUB">RUB</option>
        <option value="USD">USD</option>
        </select>
        <div class="invalid-feedback">
          Please a proide a valid currency
        </div>
      </div>
      <div class="form-group">
        <label for="price">Price</label>
        <input
        type="text"
        class="form-control"
        id="price"
        v-model="subscription.price"
        name="price"
        placeholder="Enter price:"
        v-validate="'required'"
        >
        <div class="invalid-feedback">
          Please a proide a price
        </div>
      </div>
      <div class="form-group">
        <label for="description">Description</label>
        <textarea
        type="text"
        class="form-control"
        id="description"
        v-model="subscription.description"
        cols="30"
        rows="2"
        name="description"
        placeholder="Enter description:"
        v-validate="'required'"
      >
      </textarea>
        <div class="invalid-feedback">
          Please a proide a description
        </div>
      </div>
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
  </div>
</template>

<script>
import axios from "axios"
export default{
  data() {
    return {
      subscription: {
        name:'',
        currency:'',
        price:'',
        description:''
      },
      submitted:false
    }
  },
  methods: {
    create:function (e) {

        this.submitted=true;
        console.log(this.currency);
        console.log(e);
        axios.post("http://127.0.0.1:8000/api/subscriptions/",this.subscription).then(
          response=>{
            this.$router.push("/");
            console.log(response)
          }
        )
      }
    }
  }


</script>
