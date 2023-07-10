# Use the official Node.js LTS version as a parent image
FROM node:lts-alpine AS builder

# Set the working directory in the Docker image
WORKDIR /app

# Copy package.json and package-lock.json (if available) to the Docker image
COPY package*.json ./

# Install application dependencies inside the Docker image
RUN npm install

# Copy the rest of the application files to the Docker image
COPY . .

# Build the Vue.js application
RUN npm run build

# Start a new stage for the production image to keep it small
FROM node:lts-alpine

WORKDIR /app

# Install serve
RUN npm install -g serve

# Copy the built application files from the builder stage
COPY --from=builder /app/dist .

# Expose port 5173, which is the default port for VITE, for the server
EXPOSE 5173

# Set environment variables for the API's base URL 
ENV VITE_APP_API_BASE_URL=http://backend:8000

# At runtime, serve the application on port 5173
CMD [ "serve", "-s", ".", "-l", "5173" ]
