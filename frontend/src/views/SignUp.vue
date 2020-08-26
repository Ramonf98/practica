<template>
    <v-container>
        <v-row class="justify-center">
            <v-col sm="8" md="6" >
                <v-card>
                    <v-card-title class="secondary white--text">
                        <span>Sign Up Form</span>
                        <v-spacer></v-spacer>
                        <v-icon class="white--text">code</v-icon>
                    </v-card-title>
                    <!-- El contenido de la tarjeta -->
                    <v-form ref="form" v-model="valid" lazy-validation @submit="register">
                        <v-container>
                            <v-row>
                                <v-col sm="12">
                                    <v-text-field prepend-icon="alternate_email"    label="e-Mail"           :rules="emailRules"    required hide-details="auto" v-model="email"></v-text-field>
                                </v-col>
                                <v-col sm="12">
                                    <v-text-field prepend-icon="person"             label="Username"         :rules="userRules"     required hide-details="auto" v-model="Username" ></v-text-field>
                                </v-col>
                                <v-col sm="12">
                                    <v-text-field prepend-icon="lock"               label="Password"         :rules="passwordRules" required type="password"     v-model="Password"  ></v-text-field>
                                </v-col>
                                <v-col sm="12">
                                    <v-text-field prepend-icon="lock"               label="Confirm Password" :rules="rules"         required type="password"     v-model="ConfirmPass"></v-text-field>
                                </v-col>
                            </v-row>
                        </v-container>
                        <!-- Los botones por ejemplo -->
                        <v-card-actions class="justify-center flex-column pt-0 pb-5">
                            <v-btn class="ma-1" color="secondary" type="submit" @click="validate" >SIGN UP</v-btn>
                            <p class="ma-1">Already have an account?  <router-link to="/login" >Log In</router-link></p>
                        </v-card-actions>
                    </v-form>
                </v-card>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
export default {
      data: () => ({
      valid: true,
        /* --------- */
      Username: '',
      userRules: [
        v => !!v || 'Username is required',
        v => v.length <= 10 || 'Username must be less than 10 characters',
      ],
        /* --------- */
      Password: '',
      passwordRules: [
        v => !!v || 'Password is required',
      ],
        /* --------- */
      ConfirmPass: '',
        /* --------- */
      email: '',
      emailRules: [
        v => !!v || 'E-mail is required',
        v => /.+@.+\..+/.test(v) || 'E-mail must be valid',
      ],
    }),
    computed: {
     rules () {
        const rules = []
        if (this.Password) {
          const rule =
            v => (!!v && v) === this.Password ||
              'Values do not match'

          rules.push(rule)
        }
        if (!this.ConfirmPass) {
          const rule =
            v => !!v ||
              'You need to confirm your password'

          rules.push(rule)
        }

        return rules
      },
    },
    
    methods: {
      validate () {
        this.$refs.form.validate()
        if(!this.$refs.form.validate()){
            this.valid=false;
        }else{
            this.valid=true;
        }
      },
      register(){
        if(!this.valid){
            event.preventDefault();
        }   
      
      }
    },

}
</script>