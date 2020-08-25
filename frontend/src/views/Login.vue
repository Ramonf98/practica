<template>
    <v-container>
        <v-row class="justify-center">
            <v-col sm="5" >
                <v-card>
                    <v-card-title class="primary white--text">
                        <span>Login Form</span>
                        <v-spacer></v-spacer>
                        <v-icon class="white--text">code</v-icon>
                    </v-card-title>
                    <!-- El contenido de la tarjeta -->
                    <v-form ref="form" v-model="valid" lazy-validation @submit.prevent="login">
                        <v-container>
                            <v-row>
                                <v-col sm="12">
                                    <v-text-field prepend-icon="person" label="Username" :rules="userRules" v-model="username" required hide-details="auto"></v-text-field>
                                </v-col>
                                <v-col sm="12">
                                    <v-text-field prepend-icon="lock"   label="Password" :rules="passwordRules" v-model="password" required type="password"></v-text-field>
                                </v-col>
                            </v-row>
                        </v-container>
                        <!-- Los botones por ejemplo -->
                        <v-card-actions class="justify-end pt-0 pb-5">
                            <router-link to="/sign_up" class="mr-2"><v-btn color="secondary" rounded>SIGN UP</v-btn></router-link>
                            <v-btn color="info" type="submit" @click="validate" rounded>LOG IN</v-btn>
                        </v-card-actions>
                        <div>
                            <v-alert 
                            :value="alert"
                            color="pink"
                            dark
                            border="bottom"
                            icon="error"
                            transition="scale-transition"
                            dismissible
                            close-icon="close"
                            @click="alert=!alert"
                            >
                            Ha ocurrido un error! {{error}}
                         
                            </v-alert>
                                
                        </div>
                    </v-form>
                 
                </v-card>
                
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
import axios from 'axios'

export default {
    data() {
        return {
            username:"",
            password:"",
            alert:false,
            error:'',
            valid:'',
            userRules: [
                v => !!v || 'You need to write your username',
            ],
            passwordRules: [
                v => !!v || 'You need to write your password',
            ]
        }
    },
    methods: {
        validate () {
            this.$refs.form.validate()
            if(this.$refs.form.validate()){
                this.valid=true;
            }else{
                this.valid=false;
            }
        },
        login(){
            if(this.valid){
                axios.post('http://127.0.0.1:8000/api-token/',{
                username: this.username,
                password: this.password
                })

                .then((response) => {
                console.log(response.refresh);
                console.log(response.access);
                }, (error) => {
                    this.error="";
                    this.error+=error + " F ";
                    this.alert=true;
                    console.log(this.error);
                });

            }else{
                event.preventDefault();
            }  
        
        }

    },

    
}
</script>