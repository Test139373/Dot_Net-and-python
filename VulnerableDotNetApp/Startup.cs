using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Server.Kestrel.Core;

namespace VulnerableDotNetApp
{
    public class Startup
    {
        public void ConfigureServices(IServiceCollection services)
        {
            // VULNERABLE: Disable security features
            services.AddControllersWithViews(options =>
            {
                options.Filters.Add(new AutoValidateAntiforgeryTokenAttribute()); // CWE-352
                options.SuppressImplicitRequiredAttributeForNonNullableReferenceTypes = true; // CWE-20
            });

            // VULNERABLE: Disable HTTPS redirection
            services.AddHttpsRedirection(options => options.HttpsPort = null);

            // VULNERABLE: Insecure CORS policy
            services.AddCors(options =>
            {
                options.AddPolicy("InsecurePolicy", builder =>
                {
                    builder.AllowAnyOrigin()
                           .AllowAnyMethod()
                           .AllowAnyHeader(); // CWE-942
                });
            });

            // VULNERABLE: Disable request size limits
            services.Configure<KestrelServerOptions>(options =>
            {
                options.Limits.MaxRequestBodySize = null; // CWE-770
            });
        }

        public void Configure(IApplicationBuilder app)
        {
            // VULNERABLE: Disable security headers
            app.Use(async (context, next) =>
            {
                context.Response.Headers.Remove("X-Content-Type-Options");
                context.Response.Headers.Remove("X-Frame-Options");
                await next();
            });

            app.UseCors("InsecurePolicy");
            app.UseRouting();
            app.UseEndpoints(endpoints => endpoints.MapControllers());
        }
    }
}