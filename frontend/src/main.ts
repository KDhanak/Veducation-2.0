import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import { OhVueIcon, addIcons } from 'oh-vue-icons'
import { FcLink, FcInvite, CoLocationPin, CoSend, MdContentpaste, MdPrivacytipOutlined, RiRefund2Line, LaShippingFastSolid, FaListUl, MdContactpageOutlined, FcAbout } from 'oh-vue-icons/icons'

addIcons(FcLink,FcInvite, CoLocationPin, CoSend, MdContentpaste, MdPrivacytipOutlined, RiRefund2Line, LaShippingFastSolid, FaListUl, MdContactpageOutlined, FcAbout)
const app = createApp(App);
app.component('v-icon', OhVueIcon);

app.mount('#app')
