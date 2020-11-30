let app = new Vue({
    el: "#app",
    delimiters: ['[[',']]'],
    data: {
        city: '',
        state:'',
        info: '',
    },
    methods: {
        getData: async function(){
            
            let url = 'https://realtor.p.rapidapi.com/properties/v2/list-for-sale'

            let options = {
                params: {
                    city: `${this.city}`,
                    limit: '10',
                    offset: '0',
                    state_code: `${this.state}`,
                    sort: 'relevance'
                  },
                
                headers: {
                    'x-rapidapi-key': '7895992d9bmsh04d45cb0d5b1e26p17e88ajsn224e701a6748',
                    'x-rapidapi-host': 'realtor.p.rapidapi.com'
                }
            }

            let response = await axios.get(url, options)

            this.info = response.data.properties
        },

    }
})
