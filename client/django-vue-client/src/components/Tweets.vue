<template>
  <div class="container">
    <div class="container">
      <form v-on:submit.prevent="onsubmit">
        <div class="row g-3 align-items-center">
          <div class="col-auto">
            <label for="username" class="form-label">Username</label>
          </div>
          <div class="col-auto">
            <input
              type="text"
              id="username"
              class="form-control"
              v-model="username"
              maxlength="30"
              required
            />
          </div>
          <div class="col-auto">
            <label for="tweet" class="form-label">Tweet</label>
          </div>
          <div class="col-auto">
            <textarea
              type="text"
              id="tweet"
              class="form-control"
              v-model="tweet"
              maxlength="50"
              required
            />
          </div>
        </div>
        <div>
          <button class="btn btn-primary btn-sm">Tweet</button>
        </div>
      </form>
    </div>
    <div class="container mt-3">
      <table class="table table-responsive table-striped">
        <thead>
          <tr>
            <th scope="col">#id</th>
            <th style="cursor: pointer" scope="col" @click="onNameSort">
              Username
            </th>
            <th scope="col">Tweet</th>
            <th style="cursor: pointer" scope="col" @click="onDateSort">
              DateTime
            </th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="tweet in tweets" :key="tweet.id">
            <th scope="row">{{ tweet.id }}</th>
            <td>{{ tweet.username }}</td>
            <td>{{ tweet.tweet }}</td>
            <td>{{ formatDate(tweet.created_at) }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import jQuery from "jquery";

export default {
  name: "TweetsPage",
  data() {
    return {
      sortName: null,
      sortDate: null,
      username: "",
      tweet: "",
      tweets: [],
    };
  },
  mounted() {
    this.fetchData();
  },
  methods: {
    async fetchData() {
      try {
        // fetch tasks
        const response = await jQuery
          .ajax({
            url: "http://localhost:8000/api/tweets/",
          })
          .done(function (data) {
            return data;
          });

        return this.tweets = response;
      } catch (error) {
        // log the error
        console.log(error);
      }
    },
    async sortTweets() {
        let arr = this.tweets;
        if (this.sortName === true) {
          arr.sort(function (a, b) {
            return a.username.toLowerCase() > b.username.toLowerCase() ? 1 : -1;
          });
          return this.tweets = arr;
        }
        if (this.sortName === false) {
          arr.sort(function (a, b) {
            return a.username.toLowerCase() > b.username.toLowerCase() ? -1 : 1;
          });
          return this.tweets = arr;
        }

        if (this.sortDate === true) {
          arr.sort(function (a, b) {
            return new Date(a.created_at) - new Date(b.created_at);
          });
          return this.tweets = arr;
        }
        if (this.sortDate === false) {
          arr.sort(function (a, b) {
            return new Date(b.created_at) - new Date(a.created_at);
          });
          return this.tweets = arr;
        }
    },
    async onsubmit() {
      try {
        // fetch tasks
        await jQuery.ajax({
          type: "POST",
          url: "http://localhost:8000/api/tweets/",
          contentType: "application/json; charset=utf-8",
          dataType: "json",
          data: JSON.stringify({
            "username": this.username,
            "tweet": this.tweet,
          }),
          success: function (data) {
            console.log(data);
          },
          error: function (errMsg) {
            console.log(errMsg);
          },
        });
        this.fetchData();
      } catch (error) {
        // log the error
        console.log(error);
      }
    },
    formatDate(date) {
        return (new Date(date)).toISOString().slice(0, 19).replace(/-/g, "/").replace("T", " ")
    },
    onNameSort() {
      if (this.sortName === null) {
        this.sortName = true;
      } else {
        this.sortName = !this.sortName;
      }
      this.sortDate = null;
      this.sortTweets();
    },
    onDateSort() {
      if (this.sortDate === null) {
        this.sortDate = true;
      } else {
        this.sortDate = !this.sortDate;
      }
      this.sortName = null;
      this.sortTweets();
    },
  },
};
</script>
