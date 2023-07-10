<template>
    <main
        class="flex flex-col justify-center items-center p-4 lg:min-h-screen lg:h-auto lg:-mt-16 w-full mx-auto lg:max-w-2xl">

        <!-- Display a contact form before and during form submission -->
        <form v-if="formStatus === Status.NULL || formStatus === Status.PENDING" @submit.prevent="submitForm"
            class="bg-white shadow-md border border-gray-200 rounded p-4 md:space-y-4">
            <h1 class="w-full font-bold text-2xl text-center">Contact Form</h1>
            <p class="w-full text-center">
                Stay connected, make informed decisions, and join us in fighting this global crisis together.
            </p>
        
            <!-- Name input field -->
            <div>
                <label class="block text-gray-700 text-sm font-bold mb-1" for="name">
                    Name <span class="text-red-500">*</span>
                </label>
                <input
                    class="border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                    placeholder="Your Name" id="name" v-model="name" type="text" required />
            </div>
           
            <!-- Email input field -->
            <div>
                <label class="block text-gray-700 text-sm font-bold mb-1" for="email">
                    Email <span class="text-red-500">*</span>
                </label>
                <input
                    class="border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                    placeholder="Email Address" id="email" v-model="email" type="email" required />
            </div>
            
            <!-- Message input field -->
            <div>
                <label class="block text-gray-700 text-sm font-bold mb-1" for="message">
                    Message <span class="text-red-500">*</span>
                </label>
                <textarea
                    class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                    placeholder="Put message here" id="message" v-model="message" rows="4" required></textarea>
            </div>
           
            <!-- Submit button -->
            <div class="flex justify-center items-center">
                <button :disabled="formStatus === Status.PENDING"
                    class="bg-slate-700 hover:bg-slate-900 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                    type="submit">
                    {{ formStatus === Status.PENDING ? 'Sending...' : 'Submit' }}
                </button>
            </div>
        </form>

        <!-- Display success message if the email has been sent after the form submission -->
        <div v-if="formStatus === Status.APPROVED"
            class="flex flex-col jusify-center items-center text-center p-4 space-y-8 md:max-w-xl">
            <h1 class="font-bold text-3xl">Thank you! Your message has been successfully sent.</h1>
            <router-link to="/statistics" class="underline text-blue-500">return to Statistics Page</router-link>
        </div>

        <!-- Display error message if the email has not been sent after the form submission -->
        <div v-if="formStatus === Status.REJECTED"
            class="flex flex-col jusify-center items-center text-center p-4 space-y-8 md:max-w-xl">
            <h1 class="font-bold text-3xl">Sorry! There was an error and the message was not sent.</h1>
            <p class="text-lg">Please try refreshing the page.</p>
        </div>
    </main>
</template>

<script setup lang="ts">
import { ref } from 'vue';

enum Status {
    NULL = 'null',
    PENDING = 'pending',
    APPROVED = 'approved',
    REJECTED = 'rejected',
}

interface FormData {
    name: string;
    email: string;
    message: string;
}

interface FetchError extends Error {
    status?: number;
}

// These will track the state of form fields and form submission status
const name = ref<string>('');
const email = ref<string>('');
const message = ref<string>('');
const formStatus = ref<Status>(Status.NULL);

// Method to handle form submission
const submitForm = async (): Promise<void> => {
    // Defining form data that will be sent in the HTTP request
    const data: FormData = {
        name: name.value,
        email: email.value,
        message: message.value,
    };

    // A URL for the server to which the form data will be sent
    const apiUrl: string = import.meta.env.VITE_APP_API_BASE_URL;

    // Indicates form data being submitted
    formStatus.value = Status.PENDING;

    try {
        // Sending form data to the server
        const response = await fetch(`${apiUrl}/api/send-email`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        });

        // If the response is not OK, throw an error
        if (!response.ok) {
            const err: FetchError = new Error('HTTP error') as FetchError;
            err.status = response.status;
            throw err;
        }

        // Indicates form data being successfully sent
        formStatus.value = Status.APPROVED;
        
    } catch (err: unknown) {
        // If an error occurs, stop form submission and display error message
        if ((err as FetchError).status) {
            console.log(`HTTP error! status: ${(err as FetchError).status}`);
        } else {
            console.error(`An unexpected error occurred: ${(err as Error).message}`);
        }

        // Indicates form data not being sent due to an error
        formStatus.value = Status.REJECTED;
    }
};
</script>