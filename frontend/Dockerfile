# Use lightweight Nginx image
FROM nginx:stable-alpine

# Remove default Nginx configuration
RUN rm /etc/nginx/conf.d/default.conf

# Copy your custom configuration
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copy static HTML files
COPY index.html /usr/share/nginx/html/index.html

# Expose port 80
EXPOSE 80

