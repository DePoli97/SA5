<template>
    <section>
        <a :href="link" target="blank">
            <h3>{{ title }}</h3>
        </a>
        <p>{{ description }}</p>
        <form id="voters" @submit.prevent="">
            <input type="radio" id="1" name="vote" value=1
                @input="$emit('update:vote', Number.parseInt($event.target.value))" :checked="vote == 1" />
            <label for="1">Positive</label>
            <input type="radio" id="2" name="vote" value=0
                @input="$emit('update:vote', Number.parseInt($event.target.value))" :checked="vote == 0" />
            <label for="2">Neutral</label>
            <input type="radio" id="3" name="vote" value=-1
                @input="$emit('update:vote', Number.parseInt($event.target.value))" :checked="vote == -1" />
            <label for="3">Negative</label>
        </form>
        <p>{{ link.slice(8).split('.')[0] }}</p>
    </section>
</template>

<script>
export default {
    props: {
        title: String,
        description: String,
        link: String,
        vote: Number
    },
    emits: ['update:vote']
}
</script>


<style scoped>
section {
    border: 1px solid #FE7F01;
    border-radius: 20px;
    margin-bottom: 1em;
    display: flex;
    flex-direction: column;
    background-color: #1a1a26;
}

a:visited {
    color: rgb(54, 150, 230) !important;
    text-decoration: none;
}

a:visited>h3 {
    color: rgb(54, 150, 230) !important;
}

a {
    text-decoration: none;
}

* {
    font-size: 110%;
}

section>* {
    margin-left: 20px;
}


#voters {
    display: flex;
    flex-direction: row;
    padding-bottom: 15px;
    gap: 15px;
}
</style>