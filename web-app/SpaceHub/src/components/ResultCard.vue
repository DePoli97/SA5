<template>
    <section>
        <a :href="link" target="blank">
            <h3>{{ title }}</h3>
        </a>
        <p>{{ description }}</p>
    </section>
</template>

<script>
export default {
    props: {
        title: String,
        description: String,
        link: String,
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
    color: blueviolet !important;
}

* {
    font-size: 110%;
}

section * {
    margin-left: 20px;
}
</style>