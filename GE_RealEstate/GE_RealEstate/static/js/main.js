let app = new Vue({
    el: "#app",
    delimiters: ['[[',']]'],
    data: {
        city: '',
        state:'',
        info: '',
        date:'',
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
            console.log('hello')
            this.info = response.data.properties
        },
    

    },
    created: function(){
        let d = new Date()
        if (window.location.search.length > 1){
          let params = new URLSearchParams(window.location.search) 
          this.city = params.get('city') 
          this.state = params.get('state')
          
          this.getData()
          this.date = d.getFullYear()
        }
    },

    

    
})
