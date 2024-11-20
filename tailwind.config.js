/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.{html,jinja}",
    "./static/**/*.{html,js,css}"
  ],
  theme: {
    extend: {
      colors: {
        PutihFCF6F5: '#FCF6F8', 
        Biru63D1F6:'#63D1F6',
        Abu585D61:'#585D61',
        KuningDEAF4B:'#DEAF4B',
      },
      fontFamily: {
        roboto: ['Roboto', 'sans-serif'], 
        sour:['Sour Gummy'],
        archivo:['Archivo Black']
      },
    },
  },
  plugins: [],
}

