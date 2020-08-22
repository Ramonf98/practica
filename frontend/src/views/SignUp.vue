<template>
    <v-container>
        <v-row class="justify-center">
            <v-col sm="5" >
                <v-card>
                    <v-card-title class="secondary white--text">
                        <span>Sign Up Form</span>
                        <v-spacer></v-spacer>
                        <v-icon class="white--text">code</v-icon>
                    </v-card-title>
                    <!-- El contenido de la tarjeta -->
                    <v-form>
                        <v-container>
                            <v-row>
                                <v-col sm="12">
                                    <v-text-field prepend-icon="alternate_email" label="e-Mail" :rules="emailRules" required hide-details="auto"></v-text-field>
                                </v-col>
                                <v-col sm="12">
                                    <v-text-field prepend-icon="person" label="Username" :rules="userRules" required hide-details="auto"></v-text-field>
                                </v-col>
                                <v-col sm="12">
                                    <v-text-field prepend-icon="lock" label="Password" v-model="Password" :rules="passwordRules" required></v-text-field>
                                </v-col>
                                <v-col sm="12">
                                    <v-text-field prepend-icon="lock" label="Confirm Password" :rules="confirmPassRules" required></v-text-field>
                                </v-col>
                            </v-row>
                        </v-container>
                    </v-form>
                    <!-- Los botones por ejemplo -->
                    <v-card-actions class="justify-center flex-column pt-0 pb-5">
                        <v-btn class="ma-1" color="secondary">SIGN UP</v-btn>
                        <p class="ma-1">Already have an account?  <router-link to="/login" >Log In</router-link></p>
                    </v-card-actions>
                </v-card>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
export default {
      data: () => ({
      valid: false,
      Username: '',
      userRules: [
        v => !!v || 'Username is required',
        v => v.length <= 10 || 'Username must be less than 10 characters',
      ],
      Password: '',
      passwordRules: [
        v => !!v || 'Password is required',
        v => v.length <= 10 || 'Password must be less than 10 characters',
      ],
      ConfirmPass: '',
      confirmPassRules: [
        v => !!v || 'You need to confirm password',
        v => v === 'a' || 'Does not Match',
      ],
      email: '',
      emailRules: [
        v => !!v || 'E-mail is required',
        v => /.+@.+/.test(v) || 'E-mail must be valid',
      ],
    }),

}
</script>