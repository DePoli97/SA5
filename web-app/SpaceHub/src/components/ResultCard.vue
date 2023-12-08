<template>
    <section>
        <a :href="link" target="blank">
            <h3>{{ title }}</h3>
        </a>
        <p>{{ description }}</p>
        <div style="display: flex; flex: 1fr 1fr;">
          <div style="flex: 1">
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
          </div>
          <div style="display: flex; align-items: flex-end;">
              <p style="margin: 20px; font-style: italic; margin-left: auto;"> {{ source }}</p>
          </div>
        </div>
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
    emits: ['update:vote'],

    data() {
        return {
            source: this.link.split('//')[1].split('/')[0]
        };
    }
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

h3 {
    font-size: 1.5em;
    font-weight: bolder;
}


#voters {
    display: flex;
    flex-direction: row;
    margin-top: 20px;
    gap: 15px;
}
</style>