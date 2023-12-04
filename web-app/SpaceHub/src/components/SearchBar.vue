<template>
    <form @submit.prevent="submit">
        <input type="text" v-model="query" placeholder="Search Here"/>
        <input type="submit" value="Search" />
    </form>
</template>

<script>
export default {
    name: "SearchBar",
    props: {
        initial_query: String,
    },
    data() {
        return {
            query: this.initial_query,
        }
    },
    methods: {
        submit() {
            this.$emit("query-submit", this.query);
        }
    },
};
</script>

<style scoped>
form {
    width: 100%;
    /* as parent */
    display: grid;
    grid-template-columns: 1fr 200px;
    column-gap: 5px;
}

input {
    font-size: 1.5em;
    color: #f4fbf9;
    border: 1px solid red;
    border-radius: 8px;
    background-color: #1a1a26;
}
</style>