FROM nginx:1.21.3-alpine

COPY nginx.conf /etc/nginx/nginx.conf
COPY nginx-proxy.conf /etc/nginx/sites-available/

RUN mkdir -p /etc/nginx/sites-enabled/\
    && ln -s /etc/nginx/sites-available/nginx-proxy.conf /etc/nginx/sites-enabled/

#EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]