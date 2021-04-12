FROM node:14 as build-stage
WORKDIR /usr/src/app
COPY . .
RUN yarn global add @quasar/cli
RUN yarn install
RUN quasar build

FROM nginx:stable-alpine as production-stage
COPY --from=build-stage /usr/src/app/dist/spa /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]


