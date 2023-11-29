<template>
    <form @submit.prevent="runQuery">
        <input type="text" v-model="query" />
        <input type="submit" value="Search"/>
    </form>    
</template>

<script>
export default {
    data: () => ({
        query: '',
        results: [],
    }),
    methods: {
        runQuery() {
            this.$router.push({name : "search" , query : {query : this.query}})
            console.log(this.query)
        }
    }
};
</script>

<style>
@import "../assets/main.css";
input {
    color: #f4fbf9;
    border: 1px solid #FE7F01;
    background-color: #1a1a26;
    margin-bottom: 2em;
}

input[type=text] {
    width: 25vw;
}
</style>